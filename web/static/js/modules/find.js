import $ from 'jquery'

const form = $('.js-find-form')
const result = $('.js-find-result')
const modal = $('#myModal')
const isAuthed = $('html').data('user') !== ''

const onSubmit = e => {
  e.preventDefault()
  if (!isAuthed) { modal.modal('show'); return; }

  const data = Object.assign(
    ...form.serializeArray().map(d => ({ [d.name]: d.value }))
  )

  $.post('/find', data).done(handleResponse).fail(error)
}

const handleResponse = r => {
  if (r.error) { error(); return; }

  console.log(r)
  result.html(`<p class='red'>${JSON.stringify(r)}</p>`)
}

const error = () => {
  console.log('error')
}

form.on('submit', onSubmit)
