<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="description" content="" />
    <meta name="author" content="" />
    <title>Preço das Bananas</title>
	
	
	<!-- Google tag (gtag.js) -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-WK5RSDLWM2"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'G-WK5RSDLWM2');
	</script>

    <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

    <link href="css/casado.css" rel="stylesheet" />

</head>


<body>


    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Banana tracker</a>

            <div class="wrapper">
                <ul>
                    <a href="https://www.linkedin.com/in/diogo-casado">
                        <i class="fa-brands fa-linkedin" aria-hidden="true"></i></a>
                    <a href="https://github.com/diogomcasado">
                        <i class="fa-brands fa-github" aria-hidden="true"></i></a>

                </ul>
            </div>

            <!--
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link active" aria-current="page" href="#">Home</a></li>
                            <li class="nav-item"><a class="nav-link" href="#">Link</a></li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</a>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                                    <li><a class="dropdown-item" href="#">Action</a></li>
                                    <li><a class="dropdown-item" href="#">Another action</a></li>
                                    <li><hr class="dropdown-divider" /></li>
                                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                                </ul>
                            </li>
                        </ul>
                        -->
        </div>
        </div>
    </nav>

    <div class="bg-image">
        <!-- Page content-->
        <div class="container">
            <div class="text-center mt-5">
                <h1> &#127820; Preço das bananas em Portugal &#127820;</h1>
                <!-- <p class="lead">A complete project boilerplate built with Bootstrap</p> -->
                <p>Media de preços: <span class="badge text-bg-success">
                        <?php echo file_get_contents('precos/media.txt') ?>€/Kg
                    </span></p>

                <div class="container">
                    <div class="row">
                        <div class="col-sm">
                            <img class="logotipo" src="assets/continente.png" alt="Continente">
                            <button type="button" class="btn btn-dark"
                                onclick=" window.open('https://www.continente.pt/produto/banana-continente-2597619.html','_blank')">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
								Continente: <span class="badge text-bg-success">
                                    <?php echo file_get_contents('precos/continente.txt') ?>€/Kg
                                </span>
                            </button>
                        </div>

                        <div class="col-sm">
                            <img class="logotipo" src="assets/Auchan.jpg" alt="Auchan">
                            <button type="button" class="btn btn-dark"
                                onclick=" window.open('https://www.auchan.pt/pt/produtos-frescos/fruta/banana-e-frutos-tropicais/banana-importada-kg/234229.html','_blank')">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
								Auchan: <span class="badge text-bg-success">
                                    <?php echo file_get_contents('precos/auchan.txt') ?>€/Kg
                                </span>
                            </button>
                        </div>

                        <div class="col-sm">
                            <img class="logotipo" src="assets/logo_a-perinha.jpg" alt="A Perinha">
                            <button type="button" class="btn btn-dark"
                                onclick=" window.open('https://www.aperinha.pt/banana-importada-kg','_blank')">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
								A Perinha: <span class="badge text-bg-success">
                                    <?php echo file_get_contents('precos/aperinha.txt') ?>€/Kg
                                </span>
                            </button>
                        </div>

                        <div class="col-sm">
                            <img class="logotipo" src="assets/Minipreco.png" alt="Minipreco">
                            <button type="button" class="btn btn-dark"
                                onclick=" window.open('https://www.minipreco.pt/produtos/frutas-e-vegetais/frutas/uva-banana-e-kiwi/p/98','_blank')">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
								Minipreço: <span class="badge text-bg-success">
                                    <?php echo file_get_contents('precos/minipreco.txt'); ?>€/Kg
                                </span>
                            </button>
                        </div>
                    </div>
					
					<div class="daily_graph">
                        <img src="graph.png" alt="Daily Graph">
                    </div>

                    <div class="last_update">
                        <p>Última atualização: <span class="badge text-bg-dark">
                                <?php echo file_get_contents('precos/last_update.txt'); ?>
                            </span>

                        </p>
                    </div>
                </div>
            </div>

            <div style="display: flex;justify-content: center; align-items: center; text-align: center;">
                <a class="github-button" href="https://github.com/diogomcasado"
                    data-color-scheme="no-preference: dark_dimmed; light: dark_dimmed; dark: dark_dimmed;"
                    data-size="large" aria-label="Follow @diogomcasado on GitHub">Follow @diogomcasado</a>
            </div>




        </div>

    </div>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
        crossorigin="anonymous"></script>

    <script src="https://kit.fontawesome.com/45e6481bb2.js" crossorigin="anonymous"></script>

    <script async defer src="https://buttons.github.io/buttons.js"></script>

    <!--<script src="js/scripts.js"></script>-->

</body>

</html>