const puppeteer = require('puppeteer');

function delay(time) {
    return new Promise(function(resolve) { 
        setTimeout(resolve, time)
    });
}

(async function main() {
    try {
        var date = new Date();

        var month = date.getMonth() + 1;
        var year =  date.getFullYear();
        var day = date.getDate();

        day = 30;
        month = 11
        year = 2019
        //month = 3;
        //year = 2019;

        //cases for getting previous day from current day
        if(day == 1 && month == 1){
            day = 31
            month = 12
            year = year - 1
        }
        else if(day == 1 && month == 2){
            day = 31
            month = 1
        }
        else if(day == 1 && month == 3 && year % 4 == 0){
            if(year % 400 == 0){
                day = 29
                month = 2
            }
            else if (year % 100 == 0){
                day = 28
                month = 2
            }
            else{
                day = 29
                month = 2
            }
        }
        else if(day == 1 && month == 3 && year % 4 != 0){
            day = 28
            month = 2
        }
        else if (day == 1 && month == 4){
            day = 31
            month = 3
        }
        else if (day == 1 && month == 5){
            day = 30
            month = 4
        }
        else if (day == 1 && month == 6){
            day = 31
            month = 5
        }
        else if (day == 1 && month == 7){
            day = 30
            month = 6
        }
        else if (day == 1 && month == 8){
            day = 31
            month = 7
        }
        else if (day == 1 && month == 9){
            day = 31
            month = 8
        }
        else if (day == 1 && month == 10){
            day = 30
            month = 9
        }
        else if (day == 1 && month == 11){
            day = 31
            month = 10
        }
        else if (day == 1 && month == 12){
            day = 30
            month = 11
        }
        else{
            day = day - 1
            //month = month - 1
            //console.log("herehereherehereherehereherehereherehereherehere")
        }
        

        /////////////////////////////////////////////////////////////////
        if(month < 10){
            month_ = 1 
        }
        else{
            month_ = 0
        }
        console.log('month: ' + month);

        if (day < 10){
            day_ = 1 
        }
        else{
            day_ = 0
        }
        console.log('day: ' + day);
        console.log('year: ' + year);
        
        const fillOrNot = ['', '0'];
        const text = 'https://stats.nba.com/gamebooks/?Date=' + fillOrNot[month_] + month + '%2F' + fillOrNot[day_] + day + '%2F' + year
        console.log('text: ' + text);


        ////////////////////////////////////////////////////////////////////////////////
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();

        page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')

        ////////////
        await page.goto(text);



        await page.waitForSelector('.nba-stat-table__overflow');
        

        //console.log('its showing');
        const tables = await page.$$('.nba-stat-table__overflow');
        //console.log(tables.length);

        /*
        await page.waitFor(5000)
        console.log("before");
        console.log("after");


        for (const table of tables) {
            console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            const button = await table.$('a.https://statsdmz.nba.com/pdfs/20200124/20200124_MEMDET');
            console.log("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");
            button.click();
        }

        const pdf = await page.pdf({path: 'puppdf.pdf'});

        


        //const thing = await page.$('i.stats-section-title__nav-button.fa.fa-chevron-left');
        //console.log(thing.length)

        //thing.click();
        */

        //////////getUhrefs////////////
        // way 1
        const hrefs1 = await page.evaluate(
            () => Array.from(
            document.querySelectorAll('a[href]'),
            a => a.getAttribute('href')
            )
        );
    
        // way 2
        const elementHandles = await page.$$('a');
        const propertyJsHandles = await Promise.all(
            elementHandles.map(handle => handle.getProperty('href'))
        );
        const hrefs2 = await Promise.all(
            propertyJsHandles.map(handle => handle.jsonValue())
        );
    
        console.log(hrefs1, hrefs2);
    
        // Requiring fs module in which 
        // writeFile function is defined. 
        const fs = require('fs')
        
        // Data which will write in a file. 
        //let data = "Learning how to write in a file."
    
        // Write data in 'Output.txt' . 
        fs.writeFile('Output.txt', hrefs1, (err) => {
            
            // In case of a error throw err.
            if (err) throw err;
        })
        fs.writeFile('Output2.txt', hrefs2, (err) => {
            
            // In case of a error throw err.
            if (err) throw err;
        })
        //fs.close;

        await delay(10000);

        page.waitFor(10000);
        console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")



           /////////Filter for NBA Box Scores///////////////////////
        var fsY = require("fs");
        var textY = await fsY.readFileSync("./Output2.txt");
        var textByComma = textY.toString().split(",")

            //console.log(textByComma)

        const ttt = ['LAK', 'CPS', 'GBO', 'DEL', 'MNE', 'LIN', 'RAP', 'MHU', 'RGV', 'SXF', 'STO', 'SLC', 'WIS', 'SCW', 
        'NAS', 'ACC', 'MNE', 'WES', 'FWN', 'SBL', 'CCG', 'CTN', 'ERI', 'DEL', 'LAK', 'GBO', 'AUS', 'MHU',
        'RGV', 'SXF', 'GRD', 'WCB', 'CPS', 'TEX', 'WIS', 'STO', 'SBL', 'SCW', 'WCB', 'CCG', 'IWA', 'ERI',
        'TEX', 'OKL', 'NAS', 'ACC', 'LAK', 'CTN', 'SBL', 'LIN', 'GBO', 'RAP', 'DEL', 'MHU', 'GRD' ,'WIS',
        'ACC', 'SLC']
        //console.log(ttt)

        const blank = []
        for (const y of ttt){
        if(blank.includes(y)){
        //console.log(blank)
        } else{
        blank.push(y)
        }
        }

        //console.log(blank)
        var rrr = 0
        var ccc = 0
        var goodStuff = []
        
        for (const item of textByComma){
        
        for (const bbb of blank){
        ttff = item.includes('_'+ bbb)
        ttff2 = item.includes(bbb + '.')
        if(ttff == true || ttff2 == true){
            rrr = rrr + 1
        }
        }
        if(rrr > 0){
        //console.log("Contains!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        } else{
        //console.log(item)
        const zzz = "https://statsdmz.nba.com/pdfs/"
        eee = item.includes(zzz)
        //console.log(eee)

        if(eee == true){
            goodStuff.push(ccc)
            console.log(item)
            console.log(eee)
        }
        }
        rrr = 0

        ccc = ccc + 1
        }
        console.log('YEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYEYE')
        console.log("goodStuff: " + goodStuff)//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<=======================
        console.log("goodStuff.length: "+ goodStuff.length)
        console.log("ttt: " + ttt)
        console.log("ttt.length:" + ttt.length)
        console.log("blank: " + blank) 
        console.log("blank.length: " + blank.length)

        console.log('ROWROWROWROWROWROWROWROWROWROWROWROWROWROWROWROWROWROW')
        for (const num of goodStuff){
            console.log(textByComma[num])
        }
        console.log('TIMBERTIMBERTIMBERTIMBERTIMBERTIMBERTIMBERTIMBERTIMBER')

        function removeBook(goodStuff){
            var arrayy = []
            for (const num of goodStuff){
                console.log(textByComma[num])

                if(true == textByComma[num].includes('_book.')){
                console.log("contains!!!!!!!!")
                } else {
                arrayy.push(num)
                }

            }
            return arrayy;


        }
        console.log('TIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDOTIDO')

        const goodStuffNoBooks = await removeBook(goodStuff)
        const poof = await removeBook(goodStuffNoBooks)
        console.log(poof);


        /////////////////////////
        'use strict'
        
        const Path = require('path')
        
        const Axios = require('axios')
        
        async function download(name) {
        
            const url = name
        
            const outputFileName = url.split('/')
        
            var num = outputFileName.length
            num = num - 1
            
            await console.log('outputFileName[num]: ' + outputFileName[num])
        
            const path = Path.resolve(__dirname, outputFileName[num])
            //const path = Path.resolve(__dirname, 'imageBOSCLE.pdf')
        
            const response = await Axios({
                
                method: 'GET',
        
                url: url,
        
                responseType: 'stream'
            })
        
            response.data.pipe(fs.createWriteStream(path))
        
            return new Promise((resolve, reject) => {
                response.data.on('end', () => {
                    resolve()
                })
        
                response.data.on('error', err => {
                    reject(err)
                })
            })
        }
        
        for (const poof_ of poof){
            var a = Math.floor((Math.random() * 16348) + 7819);
            console.log("delay: " + a + " milliseconds")
            await delay(a);
            //console.log("goodStuff[poof_]: " + goodStuff[poof_])
            console.log("textByComma[poof_]: " + textByComma[poof_])
            await download(textByComma[poof_])
        }
        


    } catch (e) {
        console.log('our error', e);
    }
})();












