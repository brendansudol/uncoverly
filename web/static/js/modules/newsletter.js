var $ = require('jquery');


var Newsletter = {
    form: $('#newsletter'),
    endpoint: '/newsletter',
    csrf: $('html').data('csrf'),

    init: function() {
        var self = this;

        this.form.submit(function(e) {
            e.preventDefault();
            self.submit();
        });
    },

    submit: function() {
        var self = this;

        var data = {
            'email': this.form.find('input').val(),
            'csrfmiddlewaretoken': this.csrf
        };

        var posting = $.post(this.endpoint, data);
        posting.done(function(r) { self.handleResponse(r); })
        posting.fail(function() { self.fail(); });
    },

    handleResponse: function(r) {
        if (r.outcome == 'success') this.success();
        else this.fail();
    },

    success: function(action) {
        this.form.find('button').html('✔');
    },

    fail: function() {
        console.log('subscribe fail :(');
    },
}


Newsletter.init();
