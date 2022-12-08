odoo.define('zpl_label_designer.exceptions', function () {
  class ServerError extends Error {
    constructor(title, message) {
      super(message);

      this.title = title;
    }
  }
  return {
    ServerError,
  };
});
