import $ from 'jquery'

const form = $('.js-find-form')
const result = $('.js-find-result')
const modal = $('#myModal')
const isAuthed = $('html').data('user') !== ''
const msgs = {
  already_live: 'You have great taste — that product is already on Uncoverly.',
  already_suggested: 'Great minds think alike — that product has already been suggested.',
  fail: 'Sorry! We don’t recognize that Etsy listing.',
  success: 'Thanks! We’ll take a look and let you know if it’s added.',
  error: 'Uh-oh! Something went wrong. Please try again later.',
}

const show = msg => result.html(`<p class='bg-darken-1 p2 h6'>${msg}</p>`)

const onSubmit = e => {
  e.preventDefault()
  if (!isAuthed) return modal.modal('show')

  const data = Object.assign(
    ...form.serializeArray().map(d => ({ [d.name]: d.value }))
  )

  $.post('/find', data).done(handleResponse).fail(() => show(msgs.error))
}

const handleResponse = r => {
  form.find('input[name=url]').val('')
  show(msgs[r.status] || msgs.error)
}

form.on('submit', onSubmit)
