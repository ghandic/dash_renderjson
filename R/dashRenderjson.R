# AUTO GENERATED FILE - DO NOT EDIT

dashRenderjson <- function(id=NULL, data=NULL, max_depth=NULL, theme=NULL, invert_theme=NULL) {
    
    props <- list(id=id, data=data, max_depth=max_depth, theme=theme, invert_theme=invert_theme)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashRenderjson',
        namespace = 'dash_renderjson',
        propNames = c('id', 'data', 'max_depth', 'theme', 'invert_theme'),
        package = 'dashRenderjson'
        )

    structure(component, class = c('dash_component', 'list'))
}
