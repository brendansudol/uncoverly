import $ from 'jquery'

const form = $('.js-newsletter-form')

const fail = () => console.log('subscibe fail :(')

const onSubmit = e => {
  e.preventDefault()
  const data = Object.assign(
    ...form.serializeArray().map(d => ({ [d.name]: d.value }))
  )
  $.post('/newsletter', data).done(handleResponse).fail(fail)
}

const handleResponse = r => {
  if (r.status !== 'success') return fail()
  form.find('button').html('✔')
}

form.on('submit', onSubmit)
