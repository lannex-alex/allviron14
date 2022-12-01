odoo.define('zpl_label_designer.exceptions', function (require) {
  "use strict";

  class ServerError extends Error {
    constructor(title, message) {
      super(message);

      this.title = title;
    }
  }
  return {
    ServerError
  };
});
