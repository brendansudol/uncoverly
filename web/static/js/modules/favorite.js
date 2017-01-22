var $ = require('jquery');


var Favorite = {
    endpoint_base: '/favorite/',
    csrf: $('html').data('csrf'),
    signed_out: !$('html').data('user'),

    init: function() {
        var self = this;

        $('.js-favorite').click(function(e) {
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

        var url = this.endpoint_base + this.issue_id,
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
        var ico = this.$btn.find('img'),
            src = action === 'add' ? 'like-yes' : 'like-no';

        ico.attr('src', '/static/img/ico/' + src + '.svg');
    },

    updateFail: function(reason) {
        if (!reason) reason = 'no_reason_given';
        console.log('fave fail: ' + reason);
    },
}


Favorite.init();
