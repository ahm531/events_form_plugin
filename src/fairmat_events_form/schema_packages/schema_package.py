from typing import TYPE_CHECKING

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory, EntryData
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
class RequestStatus(ArchiveSection):
    """
    A subsection for updating the status of the request - to be used only by 
    the Outreach and Adminstration admins.
    """

    status = Quantity(
        type=MEnum(
            'Under review',
            'Approved',
            'Rejected',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='what is the current status of the request'
        )
    
    reimbursement_source = Quantity(
        type=MEnum(
            'HU',
            'FAIR-DI',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
        description='How will the event expenses be covered'
        )

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
    total_expenses = Quantity(
        type=float,
        description='Automatically calculated total expenses',
    )

    def normalize(self, archive, logger):
        """
        Compute total expenses automatically during normalization.
        """
        travel = self.travel_expenses_amount or 0
        accom = self.accommodation_expenses_amount or 0
        other = self.other_expenses_amount or 0
        self.total_expenses = travel + accom + other

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


class ApplicantInformation(Schema):
    """
    An Entry for requesting an approval to attend an external event.
    """

    m_def = Section(
        label='Event Participation Request',
        categories=[UseCaseElnCategory],
    )

    
    full_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Requestor full name',
        default='FirstName LastName',
        label='Full Name'
        )
    
    email = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Applicant Email'
        )
    
    submission_date = Quantity(
        type=Datetime,
        a_eln=dict(component='DateTimeEditQuantity'),
        description='Date of submission'
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
    section_def=EventInformation,
    description='',
    repeats=False,
    )

    expected_expenses = SubSection(
    section_def='EventExpenses',
    description='',
    repeats=False,
    )

    status = SubSection(
    section_def='RequestStatus',
    label='Status - To be filled only by Outreach and Adminstration admins',
    description='',
    repeats=False,
    )


m_package.__init_metainfo__()
