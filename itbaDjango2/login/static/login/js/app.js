// CAMBIO TABS MENU //
const client = document.getElementById('client')
const noClient = document.getElementById('noClient')
const formLogin = Array.from(document.querySelectorAll('.form-login'))
const buttonJs = document.querySelectorAll('.button-js')

buttonJs.forEach(btn => {
    btn.addEventListener('click', (e) => {
        let number = e.target.dataset.number
        if (number <= 2) {
            number === '1' ? changesClassBtnClient() : changesClassBtnNoClient()
        } else {
            number === '3' ? number= "1" : number= "2"
        }
        searchParity(number)
    })
    
})

const searchParity = (value) => {
    formLogin.map(index => {
        index.classList.remove('show')
        index.dataset.section === value ? index.classList.add('show') : ""
    })
}
const changesClassBtnClient = () => {
    client.classList.add('active')
    noClient.classList.remove('active')
}
const changesClassBtnNoClient = () => {
    client.classList.remove('active')
    noClient.classList.add('active')
}