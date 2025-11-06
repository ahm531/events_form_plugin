from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Dashboard,
    Layout,
    Menu,
    MenuItemPeriodicTable,
    MenuItemHistogram,
    MenuItemTerms,
    SearchQuantities,
    WidgetHistogram,
)

schema = 'fairmat_events_form.schema_packages.schema_package.ApplicantInformation'

events_request_app_entry_point = AppEntryPoint(
    name = 'Events Requests App',
    description = 'This app is to track the submitted events requests by FAIRmat members',
    app = App(
        label='Events Requests',
        path='eventsapp',
        category='Use Cases',
        description='Track the events requests from FAIRmat members',
        search_quantities=SearchQuantities(include=[f'data.*#{schema}', f'metadata.*#{schema}']),
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
                label='Area',
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
                    title='Requestor',
                    items=[
                    MenuItemTerms(
                    quantity=f'data.fairmat_area#{schema}',
                    title='FAIRmat Area',
                    show_input=False,
                    ),
                    MenuItemTerms(
                    quantity=f'data.full_name#{schema}',
                    title='Name',
                    show_input=False,
                    ),
                    MenuItemTerms(
                    quantity=f'data.role_at_fairmat#{schema}',
                    title='role',
                    show_input=False,
                    ),
                    ]
                )
            ]
        )
        )
)