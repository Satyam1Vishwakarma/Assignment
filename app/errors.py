def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return {"error": "Bad Request"}, 400

    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not Found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal Server Error"}, 500