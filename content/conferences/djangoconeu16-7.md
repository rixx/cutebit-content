Title: DjangoCon Europe 2016 - Going with the Flow with Django Admin
Date:   2016-03-31
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "Going with the Flow with Django Admin"


**Speaker:** Maria Lowas-Rzechonek ([twitter](https://twitter.com/marialowas)) Django developer and involved with Django
Girls.

## Goals

Model workflows in Django Admin.

 - Add custom workflow-related fields
 - Add custom URLs
 - Override default templates
 - add a column to the ListView with a calculated column


## Methods

 - use fieldsets to separate content from workflow data
 - write methods for each transition in the state model
 - add get_urls(return my_urls + super_urls)
 - change `templates/damin/bla/keks/change_form.html` to make workflow actions appear in the toolbar
 - add calculated column to list
    - write method calculating the value
    - `method.boolean = True` for icons
    - `method.admin_order_field = 'method'` for ordering
    - use an annotated queryset:
        
        class Greater(CombinedExpression):
            def __init__self, lhs, rhs):
                super(Greater, self).__init__(lhs, '>', rhs, output_field=BooleanField)

        in manager: use Greater in get_queryset
 - add some css

For further information, watch [Pushing the Pony's Boundaries](https://vimeo.com/134817269) from last year's DjangoCon
Europe.
