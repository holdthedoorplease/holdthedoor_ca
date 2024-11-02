---
myst:
  html_meta:
    "description lang=en": |
      Documentation for users who wish to build sphinx sites with
      pydata-sphinx-theme.
---

# Visit Canada

Explore the various types of visitor visas to Canada and find the one that best suits your needs.

```{gallery-grid}
:grid-columns: 1 2 2 3

- header: "{fas}`book;pst-color-primary` Study in Canada"
  content: "Pursue your education in Canada with our Student Visa information."
  link: study/index

- header: "{fas}`plane;pst-color-primary` Travel to Canada"
  content: "Plan your vacation with ease using our Tourist Visa resources."
  link: travel/index

- header: "{fas}`users;pst-color-primary` Visit Family in Canada"
  content: "Learn about visas to visit your family members in Canada, including the Super Visa."
  link: supervisa/index

- header: "{fas}`briefcase;pst-color-primary` Work in Canada"
  content: "Find opportunities to work in Canada through our Work Visa guides."
  link: work/index

- header: "{fas}`handshake;pst-color-primary` Visit Canada on Business"
  content: "Explore options for business visitors and entrepreneurs."
  link: business/index

- header: "{fas}`info-circle;pst-color-primary` All Visitor Visas"
  content: "Find information on all types of visitor visas to Canada."
```


There are a number of options for configuring your site's look and feel.
All configuration options are passed with the `html_theme_options` variable in your `conf.py` file.
This is a dictionary with `key: val` pairs that you can configure in various ways.

```{toctree}
:maxdepth: 2
:caption: Study in Canada

study/index
```

```{toctree}
:maxdepth: 2
:caption: Travel to Canada

travel/index
```

```{toctree}
:maxdepth: 2
:caption: Super Visa

supervisa/index
```

```{toctree}
:maxdepth: 2
:caption: Work in Canada

work/index
```

```{toctree}
:maxdepth: 2
:caption: Business in Canada

business/index
```