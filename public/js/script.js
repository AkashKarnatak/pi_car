const socket = io()
const $ = (x) => document.querySelector(x)

$forward_button = $('#forward')
$left_button = $('#left')
$right_button = $('#right')
$back_button = $('#back')

$forward_button.addEventListener("click", () => {
	console.log('forward button clicked')
	socket.emit('forward')
})

$left_button.addEventListener("click", () => {
	console.log('left button clicked')
	socket.emit('left')
})

$right_button.addEventListener("click", () => {
	console.log('right button clicked')
	socket.emit('right')
})

$back_button.addEventListener("click", () => {
	console.log('back button clicked')
	socket.emit('back')
})
