from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemTerms,
    SearchQuantities,
)

schema = 'fairmat_events_form.schema_packages.\
    schema_package.ApplicantInformation'

events_request_app_entry_point = AppEntryPoint(
    name = 'Events Requests App',
    description = 'This app is to track the submitted events \
        requests by FAIRmat members',
    app = App(
        label='Events Requests',
        path='eventsapp',
        category='Use Cases',
        description='Track the events requests from FAIRmat members',
        search_quantities=SearchQuantities(include=[f'data.*#{schema}',\
                                                     f'metadata.*#{schema}']),
        columns=[
            Column(
                quantity=f'data.full_name#{schema}',
                label='Name',
                selected=True,
            ),
            Column(
                quantity=f'data.role_at_fairmat#{schema}',
                label='Role',
                selected=True,
            ),
            Column(
                quantity=f'data.fairmat_area#{schema}',
                label='Area',
                selected=True,
            ),
            Column(
                quantity=f'data.event_details.event_name#{schema}',
                label='Event name',
                selected=True,
            ),
            Column(quantity='entry_create_time',
                label='Creation Time',
                selected=True)
        ],
        menu = Menu(
            title='Terms Filters',
            items=[
                #filter by Area
                Menu(
                    title='Requestor Information',
                    items=[
                    MenuItemTerms(
                    quantity=f'data.full_name#{schema}',
                    title='Name',
                    show_input=False,
                    ),

                    MenuItemTerms(
                    quantity=f'data.fairmat_area#{schema}',
                    title='FAIRmat Area',
                    show_input=False,
                    ),

                    MenuItemTerms(
                    quantity=f'data.role_at_fairmat#{schema}',
                    title='role',
                    show_input=False,
                    ),
                    ]
                ),
                Menu(
                    title='Request Status',
                    items=[
                    MenuItemTerms(
                    quantity=f'data.status.status#{schema}',
                    title='Status',
                    show_input=False,
                    ),
                    MenuItemTerms(
                    quantity=f'data.status.reimbursement_source#{schema}',
                    title='Paid from',
                    show_input=False,
                    ),
                    ]
                )
            ]
        )
        
        )
)