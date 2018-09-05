from app import createAdminApp

if __name__ == "__main__":
  app = createAdminApp()
  app.run(debug = True, host = "0.0.0.0")