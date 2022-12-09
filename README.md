# contact-form
[![Shinylive Deployment](https://github.com/dmolitor/contact-form/actions/workflows/shinylive.yml/badge.svg)](https://github.com/dmolitor/contact-form/actions/workflows/shinylive.yml)

This demonstrates how to create and deploy a Shiny app via Github pages by using
[Shiny for Python](https://shiny.rstudio.com/py/) and
[Shinylive](https://shiny.rstudio.com/py/docs/shinylive.html). Unfortunately this particula app doesn't
actually work because Shinylive is built on Pyodide, thus
[sockets aren't available](https://shinylive.io/py/examples/#fetch-data-from-a-web-api),
and you can't query a web API (the GMail API in this case) 😢.
