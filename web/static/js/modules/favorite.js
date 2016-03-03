var $ = require('jquery');


var Favorite = {
    fave_endpoint: '/favorite/',
    csrf: $('html').data('csrf'),
    signed_out: !$('html').data('user'),
    ico: 'ion-ios-heart',
    ico_o: 'ion-ios-heart-outline',

    init: function() {
        var self = this;

        $('.favorite').click(function(e) {
            self.handleClick(e, this);
        });
    },

    handleClick: function(e, btn) {
        e.preventDefault();

        this.$btn = $(btn);
        this.issue_id = this.$btn.data('id');

        if (this.signed_out) this.showModal();
        else this.updateAttempt();
    },

    showModal: function() {
        $('#myModal').modal('show');
    },

    updateAttempt: function() {
        var self = this;

        var url = this.fave_endpoint + this.issue_id,
            data = {'csrfmiddlewaretoken': this.csrf};

        var posting = $.post(url, data);
        posting.done(function(r) { self.handleResponse(r); })
        posting.fail(function() { self.updateFail(); });
    },

    handleResponse: function(r) {
        if (r.status == 'success') this.updateSuccess(r.action);
        else this.updateFail(r.reason);
    },

    updateSuccess: function(action) {
        var ico = this.$btn.find('i'),
            faved = action == 'add';

        var rem_cls = faved ? this.ico_o : this.ico,
            add_cls = faved ? this.ico : this.ico_o;

        ico.removeClass(rem_cls).addClass(add_cls);
    },

    updateFail: function(reason) {
        if (!reason) reason = 'no_reason_given';
        console.log('fave fail: ' + reason);
    },
}


Favorite.init();
