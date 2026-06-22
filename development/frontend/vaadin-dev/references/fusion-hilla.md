# Vaadin Fusion / Hilla Reference

## @BrowserCallable endpoint (Hilla)

```java
@BrowserCallable
@AnonymousAllowed
public class PersonEndpoint {

    private final PersonService service;

    public PersonEndpoint(PersonService service) {
        this.service = service;
    }

    public List<PersonDto> findAll() {
        return service.findAll();
    }

    public PersonDto save(PersonDto dto) {
        return service.save(dto);
    }
}
```

## React view calling Hilla endpoint

```tsx
// Generated types are in frontend/generated/
import { PersonEndpoint } from 'Frontend/generated/endpoints';
import Person from 'Frontend/generated/com/example/PersonDto';

export default function PersonView() {
  const [persons, setPersons] = useState<Person[]>([]);

  useEffect(() => {
    PersonEndpoint.findAll().then(setPersons);
  }, []);

  return (
    <Grid items={persons}>
      <GridColumn path="name" header="Name" />
    </Grid>
  );
}
```

## Lit web component with Vaadin Flow integration

```typescript
// frontend/my-widget.ts
import { LitElement, html, css } from 'lit';
import { customElement, property } from 'lit/decorators.js';

@customElement('my-widget')
export class MyWidget extends LitElement {
  @property() label = '';

  render() {
    return html`<div class="widget">${this.label}</div>`;
  }
}
```

```java
// Java side
@Tag("my-widget")
@JsModule("./my-widget.ts")
public class MyWidget extends Component {
    public void setLabel(String label) {
        getElement().setProperty("label", label);
    }
}
```

## Type generation

Run `mvn vaadin:build-frontend` or `./mvnw` to regenerate TypeScript types from Java DTOs.
Types output to `frontend/generated/`.

## Signals (Hilla reactive state, Vaadin 24.4+)

```typescript
import { signal, effect } from '@vaadin/hilla-react-signals';

const count = signal(0);
effect(() => console.log('Count changed:', count.value));
count.value++;  // triggers effect
```
