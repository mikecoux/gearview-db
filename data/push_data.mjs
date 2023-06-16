import { db, client } from "../db/conn.mjs";

async function push (colName, data) {
    try {
        const col = db.collection(`${colName}`)
        // this option prevents additional documents from being inserted if one fails
        const options = { ordered: true };
        
        // console.log(data[0])
        // console.log(typeof data)

        // const result = await col.insertOne(JSON.parse(data[0]))
        const result = await col.insertMany(data, options)
        console.log(`${result.insertedCount} documents were inserted`)
    } finally {
        await client.close()
    }
}

export default push;