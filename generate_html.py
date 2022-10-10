import webbrowser


def similar_items(data, index, algorithm):
    one = data.loc[index]['IMG_URI']
    similar_arts = data.loc[index]['SIMILAR ARTS']

    for i, art in enumerate(similar_arts):
        if i == 0:
            two = data.loc[art-1]['IMG_URI']
        if i == 1:
            three = data.loc[art-1]['IMG_URI']
        if i == 2:
            four = data.loc[art-1]['IMG_URI']
        if i == 3:
            five = data.loc[art-1]['IMG_URI']
        if i == 4:
            six = data.loc[art-1]['IMG_URI']

    f = open('template/related_arts.html', 'w')
    style = """<style>
        body {background-color: rgba(46,46,46,1);}
        .card-image {width:100%; min-height: 350px; max-height: 350px; object-fit:cover;}
    </style>"""

    msg = """ <html lang="en">
        <head>
            <title> {} </title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            {}
        </head>
        <body>
            <div class="d-flex justify-content-center">
                <div class="row">
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">Main object</p>
                        </div>
                    </div>                
                </div>
            </div>
            
            <div class="d-flex justify-content-center">  
                <div class="row">
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">#1 Similar</p>
                        </div>
                    </div> 
                    
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">#2 Similar</p>
                        </div>
                    </div> 
                    
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">#3 Similar</p>
                        </div>
                    </div> 
                    
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">#4 Similar</p>
                        </div>
                    </div> 
                    
                    <div class="card" style="width: 18rem; background-color: rgba(46,46,46,1); border-color: rgba(46,46,46,1);">
                        <img src="../{}" class="rounded card-image" alt="...">
                        <div class="card-body" style="background-color: rgba(46,46,46,1);">
                            <p class="card-text" style="color: rgba(255,255,255,0.7); text-align: center;">#5 Similar</p>
                        </div>
                    </div> 
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        </body>
    </html>""".format(algorithm, style, one, two, three, four, five, six)

    f.write(msg)
    f.close()
    webbrowser.open('template/related_arts.html', new=2)
