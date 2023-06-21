/*
Runs a child process to get Python objects into JS
*/

import { spawn } from 'child_process';
import push from '../dir/push_data.mjs';

function run(path) {
    const pyProg = spawn('python', [path]);
    let data = '';

    // Collect data from the script
    pyProg.stdout.on('data', (chunk) => {
        data += chunk.toString()
    });

    // Print errors to console, if any
    pyProg.stderr.on('data', (stderr) => {
        console.log(`stderr: ${stderr}`);
    });

    // When script is finished, push to Mongo
    pyProg.on('close', (code) => {
        if (data) {
            console.log("Pushing to Mongo...")
            console.log(JSON.parse(data)[0])
            // push('products', JSON.parse(data))
        }
        console.log(`child process exited with code ${code}`);
    });
}

run('./scrape_data.py')