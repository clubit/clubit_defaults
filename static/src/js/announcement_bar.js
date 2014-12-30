openerp.clubit_defaults = function(instance) {
  instance.web.WebClient.include({
    // Remove annoucement_bar.
    show_annoucement_bar: function() {
      return;
    }
  });
};
