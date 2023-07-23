from docxtpl import DocxTemplate

doc = DocxTemplate("word-template dosyası buraya")

invoict_list = [[2, "pen", 0.5, 1],
                [5, "notebook", 255, 2]]

doc.render({
    "name":"john",
    "phone": "34567",
    ...
})

#yukardaki keyler template içersindeki tanımlamalar