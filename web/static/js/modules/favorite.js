import $ from 'jquery'

const btn = $('.fave-action')
const modal = $('#myModal')
const isAuthed = $('html').data('user') !== ''
const csrf = { csrfmiddlewaretoken: $('html').data('csrf') }
const animate = {
  cls: 'is-animating',
  end: 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
}

const fail = why => console.log(`fave fail: ${why || 'no reason given'}`)

const onClick = e => {
  e.preventDefault()
  if (!isAuthed) return modal.modal('show')

  const a = $(e.currentTarget)
  $.post(`/favorite/${a.data('id')}`, csrf).done(handleResponse(a)).fail(fail)
}

const handleResponse = a => res => {
  if (res.status !== 'success') return fail(res.reason)

  if (res.action === 'add') a.addClass(animate.cls)
  a.find('.heart-cntnr').toggleClass('faved')
}

btn.on('click', onClick)
btn.on(animate.end, e => $(e.currentTarget).removeClass(animate.cls))
