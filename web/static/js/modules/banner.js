import Cookies from 'js-cookie'

const banner = document.querySelector('.js-banner')
const close = document.querySelector('.js-banner-close')

if (banner && close) {
  close.addEventListener('click', e => {
    e.preventDefault()
    banner.remove()
    Cookies.set('hide_banner', true, { expires: 14, path: '/' })
  })
}
