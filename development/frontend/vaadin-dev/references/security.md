# Vaadin Security Reference

## Spring Security + Vaadin Setup

```java
@EnableWebSecurity
@Configuration
public class SecurityConfig extends VaadinWebSecurity {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        super.configure(http);  // handles CSRF, session, Vaadin internals
        setLoginView(http, LoginView.class);
    }

    @Bean
    public UserDetailsService userDetailsService() {
        // replace with real UserDetailsService backed by DB
        return new InMemoryUserDetailsManager(
            User.withUsername("admin")
                .password("{noop}admin")
                .roles("ADMIN")
                .build()
        );
    }
}
```

## View-level access control

```java
@Route("admin")
@RolesAllowed("ROLE_ADMIN")     // 403 if insufficient role
public class AdminView extends VerticalLayout { ... }

@Route("public")
@PermitAll                       // any authenticated user
public class PublicView extends VerticalLayout { ... }

@Route("open")
@AnonymousAllowed               // unauthenticated allowed
public class OpenView extends VerticalLayout { ... }
```

## Security service helper

```java
@Component
public class SecurityService {

    public Optional<UserDetails> getAuthenticatedUser() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated()) return Optional.empty();
        Object principal = auth.getPrincipal();
        return principal instanceof UserDetails ud ? Optional.of(ud) : Optional.empty();
    }

    public void logout() {
        UI.getCurrent().getPage().setLocation("/logout");
    }
}
```

## XSS: never render raw HTML from user input

```java
// UNSAFE — do not use:
add(new Html("<div>" + userInput + "</div>"));

// SAFE:
add(new Text(userInput));           // escaped automatically
Span span = new Span();
span.setText(userInput);            // also safe
```

## CSRF

Vaadin's `VaadinWebSecurity` configures CSRF protection automatically for Vaadin endpoints.
Do NOT call `http.csrf().disable()` — it removes protection for all routes.
If you expose custom REST endpoints alongside Vaadin, add CSRF exemption only for those paths:

```java
http.csrf(csrf -> csrf.ignoringRequestMatchers("/api/**"));
```
