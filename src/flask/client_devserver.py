from app import createClientApp

if __name__ == "__main__":
  app = createClientApp()
  app.run(debug = True, host = "0.0.0.0")