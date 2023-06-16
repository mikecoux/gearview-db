import { spawn } from 'child_process';
import push from './push_data.mjs';

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

    // When script is finished, print collected data
    pyProg.on('close', (code) => {
        // console.log(JSON.parse(data))
        if (data) {
            console.log("Pushing to Mongo...")
            push('products', JSON.parse(data))
        }
        console.log(`child process exited with code ${code}`);
    });
}

//Run the rei_scraper file and push the data to Mongo
run('./rei_scraper.py')