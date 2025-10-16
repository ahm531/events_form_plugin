from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

from nomad.config import config
from nomad.metainfo import (
    Quantity, MSection, SubSection, MEnum, SchemaPackage
)
from nomad.metainfo.metainfo import Datetime

# Access plugin configuration
configuration = config.get_plugin_entry_point(
    'fairmat_events_form.schema_packages:schema_package_entry_point'
)

# -----------------------------
# Define schema sections
# -----------------------------

class Applicant(MSection):
    """Section 1.1 — Applicant details"""
    name = Quantity(type=str, description='Applicant full name')
    email = Quantity(type=str, description='Applicant email address')
    role_at_fairmat = Quantity(type=str, description='Role in FAIRmat (PI, Postdoc, etc.)')
    areas = Quantity(
        type=str, shape=['*'],
        description='FAIRmat Areas involved (A–G)'
    )


class EventDetails(MSection):
    """Section 1.2 — Event details"""
    event_name = Quantity(type=str)
    event_website = Quantity(type=str)
    organizer_host = Quantity(type=str)
    city_country = Quantity(type=str)
    date_start = Quantity(type=Datetime)
    date_end = Quantity(type=Datetime)
    participation = Quantity(type=str, description='How the applicant will attend')
    additional_info = Quantity(type=str, description='e.g., talk title or notes')


class ExpectedCosts(MSection):
    """Section 1.3 — Expected costs to FAIRmat"""
    travel = Quantity(type=bool)
    accommodation = Quantity(type=bool)
    other = Quantity(type=bool)
    none = Quantity(type=bool)
    details = Quantity(type=str, description='Any extra cost information')


class EventOverview(MSection):
    """Section 2.1 — Event overview"""
    title = Quantity(type=str, description='Event (working) title')
    event_type = Quantity(type=str)
    format = Quantity(type=MEnum('In-person', 'Hybrid', 'Online'))
    city_country = Quantity(type=str)
    planned_dates = Quantity(type=str)
    description = Quantity(type=str, description='Brief description and relevance to FAIRmat')


class OrganizerInfo(MSection):
    """Section 2.2 — Organizer information"""
    fairmat_organizers = Quantity(type=str, description='FAIRmat-affiliated organizers with Areas and emails')
    non_fairmat_organizers = Quantity(type=str, description='Non-FAIRmat organizers and affiliations')
    lead_contact = Quantity(type=str, description='Lead contact person')


class ParticipantInfo(MSection):
    """Section 2.3 — Participant information"""
    target_audience = Quantity(type=str)
    estimated_number = Quantity(type=int)
    fairmat_team_pis = Quantity(type=int)
    external = Quantity(type=int)


class PredictedCosts(MSection):
    """Section 2.4 — Predicted costs"""
    coffee_snacks = Quantity(type=bool)
    meals = Quantity(type=bool)
    accommodation = Quantity(type=bool)
    travel_costs = Quantity(type=bool)
    other = Quantity(type=bool)
    details = Quantity(type=str, description='Describe provided support (e.g. “lunch for 30 people”)')


class AreaFSupport(MSection):
    """Section 2.5 — Requested Area F support"""
    zoom_support = Quantity(type=bool)
    recording_editing = Quantity(type=bool)
    communication = Quantity(type=bool)
    materials = Quantity(type=bool)
    equipment = Quantity(type=bool)
    other = Quantity(type=bool)
    details = Quantity(type=str, description='Additional requests')


class SignatureSection(MSection):
    """Section 3 — Signatures"""
    applicant_signature = Quantity(type=str)
    coordinator_signature = Quantity(type=str)
    date_signed = Quantity(type=Datetime)


class EvaluationSection(MSection):
    """Section 4 — Evaluation (Areas F and G)"""
    organization = Quantity(type=str)
    costs = Quantity(type=str)
    recommendation = Quantity(type=str)
    evaluated_by = Quantity(type=str)
    date_evaluated = Quantity(type=Datetime)


class EventRequestForm(MSection):
    """Top-level form combining all sections"""
    request_type = Quantity(type=MEnum('Attend event', 'Organize event'))

    applicant = SubSection(section_def=Applicant, description='Section 1.1')
    event_details = SubSection(section_def=EventDetails, description='Section 1.2')
    expected_costs = SubSection(section_def=ExpectedCosts, description='Section 1.3')

    event_overview = SubSection(section_def=EventOverview, description='Section 2.1')
    organizer_info = SubSection(section_def=OrganizerInfo, description='Section 2.2')
    participant_info = SubSection(section_def=ParticipantInfo, description='Section 2.3')
    predicted_costs = SubSection(section_def=PredictedCosts, description='Section 2.4')
    area_f_support = SubSection(section_def=AreaFSupport, description='Section 2.5')

    signature = SubSection(section_def=SignatureSection, description='Section 3')
    evaluation = SubSection(section_def=EvaluationSection, description='Section 4')


# -----------------------------
# Schema package registration
# -----------------------------
m_package = SchemaPackage()
m_package.__name__ = 'FAIRmat Event Form'
m_package.add_section(EventRequestForm)
m_package.__init_metainfo__()
