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



# class EventOverview(MSection):
#     """Section 2.1 — Event overview"""
#     title = Quantity(type=str, description='Event (working) title')
#     event_type = Quantity(type=str)
#     format = Quantity(type=MEnum('In-person', 'Hybrid', 'Online'))
#     city_country = Quantity(type=str)
#     planned_dates = Quantity(type=str)
#     description = Quantity(type=str,
#                            description='Brief description and relevance to FAIRmat')


# class OrganizerInfo(MSection):
#     """Section 2.2 — Organizer information"""
#     fairmat_organizers = Quantity(type=str, description=
#                                   'FAIRmat-affiliated organizers with Areas and emails')
#     non_fairmat_organizers = Quantity(type=str, description=
#                                       'Non-FAIRmat organizers and affiliations')
#     lead_contact = Quantity(type=str, description='Lead contact person')


# class ParticipantInfo(MSection):
#     """Section 2.3 — Participant information"""
#     target_audience = Quantity(type=str)
#     estimated_number = Quantity(type=int)
#     fairmat_team_pis = Quantity(type=int)
#     external = Quantity(type=int)


# class PredictedCosts(MSection):
#     """Section 2.4 — Predicted costs"""
#     coffee_snacks = Quantity(type=bool)
#     meals = Quantity(type=bool)
#     accommodation = Quantity(type=bool)
#     travel_costs = Quantity(type=bool)
#     other = Quantity(type=bool)
#     details = Quantity(type=str, description=
#                        'Describe provided support (e.g. “lunch for 30 people”)')


# class AreaFSupport(MSection):
#     """Section 2.5 — Requested Area F support"""
#     zoom_support = Quantity(type=bool)
#     recording_editing = Quantity(type=bool)
#     communication = Quantity(type=bool)
#     materials = Quantity(type=bool)
#     equipment = Quantity(type=bool)
#     other = Quantity(type=bool)
#     details = Quantity(type=str, description='Additional requests')


# class SignatureSection(MSection):
#     """Section 3 — Signatures"""
#     applicant_signature = Quantity(type=str)
#     coordinator_signature = Quantity(type=str)
#     date_signed = Quantity(type=Datetime)


# class EvaluationSection(MSection):
#     """Section 4 — Evaluation (Areas F and G)"""
#     organization = Quantity(type=str)
#     costs = Quantity(type=str)
#     recommendation = Quantity(type=str)
#     evaluated_by = Quantity(type=str)
#     date_evaluated = Quantity(type=Datetime)


# class EventRequestForm(MSection):
#     """Top-level form combining all sections"""
#     request_type = Quantity(type=MEnum('Attend event', 'Organize event'))

#     applicant = SubSection(section_def=Applicant, description='Section 1.1')
#     event_details = SubSection(section_def=EventDetails, description='Section 1.2')
#     expected_costs = SubSection(section_def=ExpectedCosts, description='Section 1.3')

#     event_overview = SubSection(section_def=EventOverview, description='Section 2.1')
#     organizer_info = SubSection(section_def=OrganizerInfo, description='Section 2.2')
#     participant_info = SubSection(section_def=ParticipantInfo, description=
#                                   'Section 2.3')
#     predicted_costs = SubSection(section_def=PredictedCosts, description='Section 2.4')
#     area_f_support = SubSection(section_def=AreaFSupport, description='Section 2.5')

#     signature = SubSection(section_def=SignatureSection, description='Section 3')
#     evaluation = SubSection(section_def=EvaluationSection, description='Section 4')


# -----------------------------
# Schema package registration
# -----------------------------

m_package.__init_metainfo__()
