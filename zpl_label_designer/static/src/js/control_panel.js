odoo.define('zpl_label_designer.ControlPanel', function (require) {
  const Widget = require('web.Widget');

  const constants = require('zpl_label_designer.constants');

  const ControlPanelButtonWidget = Widget.extend({
    template: 'zpl_label_designer.ControlPanelButton',

    events: _.extend({}, Widget.prototype.events, {
      /* No events for now */
    }),

    init: function (parent, button, object) {
      this._super(parent);
      this.button = button;
      this.object = object;
    },
  });

  const ControlPanelButtonGroupWidget = Widget.extend({
    template: 'zpl_label_designer.ControlPanelButtonGroup',

    events: _.extend({}, Widget.prototype.events, {
      'click .zld-control-panel-button': '_onClick',
    }),

    init: function (parent, name, buttons, object) {
      this._super(parent);

      this.name = name;
      this.buttons = buttons;
      this.object = object;
    },

    start: function () {
      this._super();

      // Render buttons
      this.buttons.forEach((button) => {
        const buttonWidget = new ControlPanelButtonWidget(this, button, this.object);
        buttonWidget.appendTo(this.$('.zld-control-panel-group-buttons'));
      });
    },

    _onClick: function (ev) {
      const button = this.buttons.find((b) => b.name === ev.currentTarget.dataset.name);

      if (button.toggle || button.isActive(this.object)) {
        button.clickHandler(this.object);

        this.object.canvas.renderAll();

        // Re-render group of buttons to show buttons in the correct state
        this.renderElement();
        this.start();
      }
    },
  });

  const ControlPanelWidget = Widget.extend({
    template: 'zpl_label_designer.ControlPanel',

    events: _.extend({}, Widget.prototype.events, {
      /* No events for now */
    }),

    init: function (parent, canvas) {
      this._super(parent);

      this.canvas = canvas;

      /* Initial possition for debug */
      this.top = 50;
      this.left = 50;

      // Groups of buttons to render
      this.groups = [];

      // State
      this.visible = false;
    },

    show: function () {
      const changed = this._updatePosition();

      if (changed) {
        this.renderElement();
      }

      this.do_show();
      this.visible = true;
    },

    hide: function () {
      this.do_hide();
      this.visible = false;
    },

    toggle: function () {
      if (this.visible) {
        this.hide();
      } else {
        this.show();
      }
    },

    update: function (object) {
      this.object = object;

      if (object) {
        this.groups = constants.OBJECT_CONTROLS[object.type] || [];

        this._updatePosition();
        this.renderElement();
      }
    },

    getStyle: function () {
      return 'top: ' + this.top + 'px; left: ' + this.left + 'px;';
    },

    renderElement: function () {
      this._super();

      // Render groups
      this.groups.forEach((group) => {
        const groupWidget = new ControlPanelButtonGroupWidget(
          this, group.name, group.controls, this.object);
        groupWidget.appendTo(this.$('.zld-control-panel-button-groups'));
      });
    },

    _updatePosition: function () {
      const obj = this.object;
      let changed = false;

      let newTop = obj.canvas._offset.top - 10;
      let newLeft = obj.canvas._offset.left + 10;

      // Show the control panel on the right of the object
      if (obj.angle === 0) {
        newTop += obj.aCoords.tr.y;
        newLeft += obj.aCoords.tr.x;
      } else if (obj.angle === 90) {
        newTop += obj.aCoords.tl.y;
        newLeft += obj.aCoords.tl.x;
      } else if (obj.angle === 180) {
        newTop += obj.aCoords.bl.y;
        newLeft += obj.aCoords.bl.x;
      } else if (obj.angle === 270) {
        newTop += obj.aCoords.br.y;
        newLeft += obj.aCoords.br.x;
      }

      changed = this.top !== newTop || this.left !== newLeft;

      this.top = newTop;
      this.left = newLeft;

      return changed;
    },
  });

  return ControlPanelWidget;
});
