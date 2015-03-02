openerp.clubit_defaults = function(instance) {
  instance.web.WebClient.include({
    show_application: function() {
      return $.when(this._super.apply(this, arguments));
    },
    // Remove annoucement_bar.
    show_annoucement_bar: function() {
      return;
    }
  });
};
