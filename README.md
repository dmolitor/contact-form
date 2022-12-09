# contact-form
 Create a simple contact form using 
 [Shiny for Python](https://shiny.rstudio.com/py/). In theory this app could be
 deployed on a static website host (e.g. Github Pages) using 
 [Shinylive](https://shiny.rstudio.com/py/docs/shinylive.html) except for the
 fact the Shinylive is built on Pyodide, thus
 [sockets aren't available](https://shinylive.io/py/examples/#fetch-data-from-a-web-api)
 and you can't query a web API (the GMail API in this case) :(.
