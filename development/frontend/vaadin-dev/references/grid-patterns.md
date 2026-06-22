# Vaadin Grid Patterns Reference

## Component Renderer (custom cell content)

```java
grid.addColumn(new ComponentRenderer<>(person -> {
    Button btn = new Button("Edit", e -> openEditor(person));
    btn.addThemeVariants(ButtonVariant.LUMO_TERTIARY_INLINE);
    return btn;
})).setHeader("Actions");
```

## In-line Editor

```java
GridInlineEditor<Person> editor = new GridInlineEditor<>(grid);
Binder<Person> binder = editor.getBinder();
TextField nameField = new TextField();
binder.forField(nameField).bind(Person::getName, Person::setName);
editor.addColumn(binder, nameField, "Name");
editor.setBuffered(true); // only save on confirm
```

## Multi-select with SelectionListener

```java
grid.setSelectionMode(Grid.SelectionMode.MULTI);
grid.asMultiSelect().addSelectionListener(e -> {
    Set<Person> selected = e.getAllSelectedItems();
    deleteBtn.setEnabled(!selected.isEmpty());
});
```

## TreeGrid

```java
TreeGrid<Department> treeGrid = new TreeGrid<>();
treeGrid.setItems(deptService.getRoots(),
                  dept -> deptService.getChildren(dept));
treeGrid.addHierarchyColumn(Department::getName).setHeader("Department");
```

## Server-side sorting with DataProvider

```java
grid.addColumn(Person::getName)
    .setHeader("Name")
    .setSortProperty("name")   // matches DataProvider sort key
    .setSortable(true);

DataProvider<Person, Void> dp = DataProvider.fromCallbacks(
    query -> {
        List<QuerySortOrder> sort = query.getSortOrders();
        return service.fetch(query.getOffset(), query.getLimit(), sort).stream();
    },
    query -> service.count()
);
```

## Export to Excel (Apache POI)

```java
Anchor downloadLink = new Anchor(new StreamResource("export.xlsx", () -> {
    try (Workbook wb = new XSSFWorkbook()) {
        Sheet sheet = wb.createSheet("Data");
        service.findAll().forEach(item -> {
            Row row = sheet.createRow(sheet.getLastRowNum() + 1);
            row.createCell(0).setCellValue(item.getName());
        });
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        wb.write(out);
        return new ByteArrayInputStream(out.toByteArray());
    } catch (IOException e) { throw new RuntimeException(e); }
}), "Download");
downloadLink.getElement().setAttribute("download", true);
```
