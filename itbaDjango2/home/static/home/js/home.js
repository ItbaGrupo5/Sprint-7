
const valorOficialCompra = document.querySelector("#valorOficialCompra");

function traerValorOficialCompra(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        valorOficialCompra.innerHTML =`
        <h5 class="card-title">Compra</h5>
        <h3 class=" card-title fw-bold">$ ${data[0].casa.compra}</h3>
        `
    })
}

traerValorOficialCompra()

const valorOficialVenta = document.querySelector("#valorOficialVenta");

function traerValorOficialVenta(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        valorOficialVenta.innerHTML =`
        <h5 class="card-title">venta</h5>
        <h3 class=" card-title fw-bold">$ ${data[0].casa.venta}</h3>
        `
    })
}

traerValorOficialVenta()

const variacionOficial = document.querySelector("#variacionOficial");

function traerVariacionOficial(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        variacionOficial.innerHTML =`
        VARIACIÓN ${data[0].casa.variacion}
        `
    })
}

traerVariacionOficial()

const valorBlueCompra = document.querySelector("#valorBlueCompra");

function traerValorBlueCompra(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        valorBlueCompra.innerHTML =`
        <h5 class="card-title">Compra</h5>
        <h3 class=" card-title fw-bold">$ ${data[1].casa.compra}</h3>
        `
    })
}

traerValorBlueCompra()

const valorBlueVenta = document.querySelector("#valorBlueVenta");

function traerValorBlueVenta(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        valorBlueVenta.innerHTML =`
        <h5 class="card-title">venta</h5>
        <h3 class=" card-title fw-bold">$ ${data[1].casa.venta}</h3>
        `
    })
}

traerValorBlueVenta()


const variacionBlue = document.querySelector("#variacionBlue");

function traerVariacionBlue(){
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data => {
        variacionBlue.innerHTML =`
        VARIACIÓN ${data[1].casa.variacion}
        `
    })
}

traerVariacionBlue()



