import time
from typing import TYPE_CHECKING

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory
from nomad.metainfo import MEnum, Quantity, SchemaPackage
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import (
    BaseSection,
    Entity,
    EntityReference,
)
from nomad.metainfo.metainfo import Section, SubSection, Datetime, Category


if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

# Access plugin configuration
configuration = config.get_plugin_entry_point(
    'fairmat_events_form.schema_packages:schema_events_entry_point'
)

m_package = SchemaPackage()

# -----------------------------
# Define schema sections
# -----------------------------

class eventExpenses (ArchiveSection):
    """
    A subsection for providing the expected costs associated with the event.
    """

    Travel_Expenses_Description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Costs associated to traveling to the conference venue'
        )
    
    Travel_Expenses_Amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Costs associated to traveling to the event venue'
        )

    Accommodation_Expenses_Description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Costs associated to accommodation at the event city'
        )
    Accommodation_Expenses_Amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Costs associated to accommodation at the event city'
        )

    Other_Expenses_Description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Other costs associated with the event'
        )
    Other_Expenses_Amount = Quantity(
        type=float,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
        description='Other costs associated with the event'
        )

class eventInformation(ArchiveSection):
    """
    An Entry for requesting an approval to attend an external event.
    """

    Event_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='The Name of the event'
        )
    
    Event_website = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
        description='Event Website'
        )

    Event_Organizer_or_Host = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Name of the organizing entity or host'
    )

    Location= Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Event Website'
        )
    
    Event_start_date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity)
        )
    
    Event_end_date = Quantity(
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

    Participation_type = Quantity(
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
    Title_of_contribution = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant FAIRmat Area'
    )


class applicant_information(Entity, Schema):
    """
    An Entry for requesting an approval to attend an external event.
    """

    m_def = Section(
        label='Event Participation',
        categories=[UseCaseElnCategory]
    )
    Name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant full name'
        )
    
    Email = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant Email'
        )

    Role_at_fairmat = Quantity(
        type=MEnum(
            'Principal Investigator',
            'Coordinator',
            'Coworker',
            'Collaborator',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='Role in FAIRmat'
    )

    FAIRmat_Area = Quantity(
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

    Even_Details = SubSection(
    section_def='eventInformation',
    description='',
    repeats=True,
    )

    Expected_Expenses = SubSection(
    section_def='eventExpenses',
    description='',
    repeats=True,
    )


m_package.__init_metainfo__()
