const express = require('express')
const path = require('path')
const { spawn } = require('child_process')
const { Server } = require('socket.io')
const { createServer } = require('http')

const app = express()
const httpServer = createServer(app)
const io = new Server(httpServer)

io.on('connection', (socket) => {

	console.log('new connection')

	socket.on('forward', () => {

		const rccar_script = spawn(`./utils/rccar.py forward`, {shell: true})

		rccar_script.stdout.on('data', (data) => {
			console.log(`out: ${data}`)
		})

		rccar_script.stderr.on('data', (data) => {
			console.log(`err: ${data}`)
		})

		rccar_script.on('close', (code) => {
			if (code != 0) {
				return console.log('Error running the script')
			}
		})

		console.log('Ran forward script')

	})

	socket.on('left', () => {

		const rccar_script = spawn(`./utils/rccar.py left`, {shell: true})

		rccar_script.stdout.on('data', (data) => {
			console.log(`out: ${data}`)
		})

		rccar_script.stderr.on('data', (data) => {
			console.log(`err: ${data}`)
		})

		rccar_script.on('close', (code) => {
			if (code != 0) {
				return console.log('Error running the script')
			}
		})

		console.log('Ran left script')

	})

	socket.on('right', () => {

		const rccar_script = spawn(`./utils/rccar.py right`, {shell: true})

		rccar_script.stdout.on('data', (data) => {
			console.log(`out: ${data}`)
		})

		rccar_script.stderr.on('data', (data) => {
			console.log(`err: ${data}`)
		})

		rccar_script.on('close', (code) => {
			if (code != 0) {
				return console.log('Error running the script')
			}
		})

		console.log('Ran right script')

	})

	socket.on('back', () => {

		const rccar_script = spawn(`./utils/rccar.py back`, {shell: true})

		rccar_script.stdout.on('data', (data) => {
			console.log(`out: ${data}`)
		})

		rccar_script.stderr.on('data', (data) => {
			console.log(`err: ${data}`)
		})

		rccar_script.on('close', (code) => {
			if (code != 0) {
				return console.log('Error running the script')
			}
		})

		console.log('Ran back script')

	})

	socket.on('stop', () => {

		const rccar_script = spawn(`./utils/rccar.py stop`, {shell: true})

		rccar_script.stdout.on('data', (data) => {
			console.log(`out: ${data}`)
		})

		rccar_script.stderr.on('data', (data) => {
			console.log(`err: ${data}`)
		})

		rccar_script.on('close', (code) => {
			if (code != 0) {
				return console.log('Error running the script')
			}
		})

		console.log('Ran stop script')

	})

})

const port = 8080

app.use(express.static(path.join(__dirname, './public'), {extensions: ["html"]}))

httpServer.listen(port, () => {
	console.log(`Listening on port ${port}`)
})
