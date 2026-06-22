# Vaadin Advanced Routing Reference

## RouterLayout (Shell / Parent Layouts)

```java
@Route(value = "", layout = MainLayout.class)
public class DashboardView extends VerticalLayout { ... }

public class MainLayout extends AppLayout implements RouterLayout {
    public MainLayout() {
        addToNavbar(new H1("App"));
        addToDrawer(new SideNav());
    }
}
```

## Nested Routes

```java
@Route(value = "admin/users", layout = AdminLayout.class)
@RolesAllowed("ROLE_ADMIN")
public class UsersView extends VerticalLayout { ... }
```

## Error Views

```java
@Route("error")
public class CustomErrorView extends VerticalLayout
        implements HasErrorParameter<NotFoundException> {

    @Override
    public int setErrorParameter(BeforeEnterEvent event,
                                 ErrorParameter<NotFoundException> parameter) {
        add(new Text("Page not found: " + event.getLocation().getPath()));
        return HttpServletResponse.SC_NOT_FOUND;
    }
}
```

## URL Parameters

```java
// Required param: /item/42
@Route("item")
public class ItemView extends VerticalLayout
        implements HasUrlParameter<Long> {

    @Override
    public void setParameter(BeforeEvent event, Long id) {
        // load by id
    }
}

// Optional param via QueryParameters: /search?q=vaadin
@Override
public void afterNavigation(AfterNavigationEvent event) {
    event.getLocation().getQueryParameters()
         .getParameters()
         .getOrDefault("q", List.of(""))
         .stream().findFirst().ifPresent(this::search);
}
```

## Guards: BeforeEnterObserver

```java
@Override
public void beforeEnter(BeforeEnterEvent event) {
    if (!securityService.isAuthenticated()) {
        event.rerouteTo(LoginView.class);
    }
}
```

## @PreserveOnRefresh

Attach to a view to preserve component state across browser refresh.
**Warning:** All injected beans must be serializable.

```java
@Route("dashboard")
@PreserveOnRefresh
public class DashboardView extends VerticalLayout { ... }
```
