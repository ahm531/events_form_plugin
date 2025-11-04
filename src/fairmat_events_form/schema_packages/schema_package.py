from typing import TYPE_CHECKING

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import (
    Entity,
)
from nomad.metainfo import MEnum, Quantity, SchemaPackage
from nomad.metainfo.metainfo import Datetime, Section, SubSection

if TYPE_CHECKING:
    pass

# Access plugin configuration
configuration = config.get_plugin_entry_point(
    'fairmat_events_form.schema_packages:schema_events_entry_point'
)

m_package = SchemaPackage()

# -----------------------------
# Define schema sections
# -----------------------------

class EventExpenses(ArchiveSection):
    """
    A subsection for providing the expected costs associated with the event.
    """

    travel_expenses_description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Costs associated to traveling to the conference venue'
        )
    
    travel_expenses_amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Costs associated to traveling to the event venue'
        )

    accommodation_expenses_description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Costs associated to accommodation at the event city'
        )
    accommodation_expenses_amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Costs associated to accommodation at the event city'
        )

    other_expenses_description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Other costs associated with the event'
        )
    other_expenses_amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Other costs associated with the event'
        )

class EventInformation(ArchiveSection):
    """
    An Entry for requesting an approval to attend an external event.
    """

    event_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='The Name of the event'
        )
    
    event_website = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
        description='Event Website'
        )

    event_organizer_or_host = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Name of the organizing entity or host'
    )

    location= Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Event Website'
        )
    
    event_start_date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity)
        )
    
    event_end_date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity)
        )

    Attendance_method = Quantity(
        type=MEnum(
            'In-person',
            'Virtual',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='Applicant FAIRmat Area'
    )

    participation_type = Quantity(
        type=MEnum(
            'Invited talk',
            'Contributed talk/poster',
            'Booth representation',
            'User support, offer training, or demonstration',
            'Other',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='Applicant FAIRmat Area'
    )
    title_of_contribution = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant FAIRmat Area'
    )


class ApplicantInformation(Entity, Schema):
    """
    An Entry for requesting an approval to attend an external event.
    """

    m_def = Section(
        label='Event Participation',
        categories=[UseCaseElnCategory]
    )
    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant full name'
        )
    
    email = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant Email'
        )

    role_at_fairmat = Quantity(
        type=MEnum(
            'Principal Investigator',
            'Coordinator',
            'Coworker',
            'Collaborator',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='Role in FAIRmat'
    )

    fairmat_area = Quantity(
        type=MEnum(
            'A: Synthesis',
            'B: Experiments',
            'C: Computations',
            'D: Infrastructure',
            'E: Usecases',
            'F: Outreach',
            'G: Adminstration',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='Applicant FAIRmat Area'
    )

    event_details = SubSection(
    section_def='eventInformation',
    description='',
    repeats=True,
    )

    expected_expenses = SubSection(
    section_def='eventExpenses',
    description='',
    repeats=True,
    )


m_package.__init_metainfo__()
