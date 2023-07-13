<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://bootstrap-4.ru/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>Bootstrap Example</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Bootstrap Example</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  </head>
  <style>

  </style>

  <body class="p-3 m-0 border-0 bd-example">

    <!-- Example Code -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">ПоРодине</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Главная <span class="sr-only"></span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Туры</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Санкт-Петербург
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
<!--      <li class="nav-item">-->
<!--        <a class="nav-link disabled" href="#">Disabled</a>-->
<!--      </li>-->
    </ul>
      <div>
          <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Поиск" aria-label="Search">
<!--      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Поиск</button>-->
    </form>
      </div>

  </div>
</nav>

<div>
    <div id="carouselExampleCaptions" class="carousel slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2" class="active" aria-current="true"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item">
        <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Первый слайд" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"></rect><text x="50%" y="50%" fill="#555" dy=".3em">Первый слайд</text></svg>
        <div class="carousel-caption d-none d-md-block">
          <h5>Метка первого слайда</h5>
          <p>Некоторый репрезентативный заполнитель для первого слайда.</p>
        </div>
      </div>
      <div class="carousel-item active">
        <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Второй слайд" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#666"></rect><text x="50%" y="50%" fill="#444" dy=".3em">Второй слайд</text></svg>
        <div class="carousel-caption d-none d-md-block">
          <h5>Метка второго слайда</h5>
          <p>Некоторый репрезентативный заполнитель для второго слайда.</p>
        </div>
      </div>
      <div class="carousel-item">
          <img src="https://vsegda-pomnim.com/uploads/posts/2022-04/1649124844_57-vsegda-pomnim-com-p-priroda-gor-foto-68.jpg" class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" height="400"s>

<!--          <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Третий слайд" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#555"></rect><text x="50%" y="50%" fill="#333" dy=".3em">Третий слайд</text></svg>-->

        <div class="carousel-caption d-none d-md-block">
          <h5>Метка третьего слайда</h5>
          <p>Некоторый репрезентативный заполнитель для третьего слайда.</p>

        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Предыдущий</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Следующий</span>
    </button>


  </div>

</div>


<div  class="overflow-hidden">
  <div class="row row-cols-2 row-cols-lg-3 g-2 g-lg-3">
    <div class="col">
      <div class="p-3">
          <div class="card" style="width: 28rem;">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Изображение заглушка" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"></rect><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Изображение заглушка</text></svg>

                <div class="card-body">
                  <h5 class="card-title">Заголовок карточки</h5>
                  <p class="card-text">Небольшой пример текста, который должен основываться на названии карточки и составлять основную часть содержимого карты.</p>
                  <a href="index.html" class="btn btn-primary">Перейти куда-нибудь</a>
                </div>
              </div>
      </div>
    </div>
    <div class="col">
      <div class="p-3">
          <div class="card" style="width: 28rem;">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Изображение заглушка" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"></rect><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Изображение заглушка</text></svg>

                <div class="card-body">
                  <h5 class="card-title">Заголовок карточки</h5>
                  <p class="card-text">Небольшой пример текста, который должен основываться на названии карточки и составлять основную часть содержимого карты.</p>
                  <a href="index2.html" class="btn btn-primary">Перейти куда-нибудь</a>
                </div>
              </div>
      </div>
    </div>
    <div class="col">
      <div class="p-3">
          <div class="card" style="width: 28rem;">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Изображение заглушка" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"></rect><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Изображение заглушка</text></svg>

                <div class="card-body">
                  <h5 class="card-title">Заголовок карточки</h5>
                  <p class="card-text">Небольшой пример текста, который должен основываться на названии карточки и составлять основную часть содержимого карты.</p>
                  <a href="index3.html" class="btn btn-primary">Перейти куда-нибудь</a>
                </div>
              </div>
      </div>
    </div>
</div>
</div>
    <!-- End Example Code -->
    </body>
</html>
