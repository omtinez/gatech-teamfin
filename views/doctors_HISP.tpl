% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
	<h2>{{ title }}</h2>
	<h3>{{ message }}</h3>
	<form action="/doctors_HISP" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <input name="hispAddress" class="form-control" id="email" placeholder="Enter your doctors HISP address">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Submit" type="submit" class="btn btn-primary active"/>
      </div>
    </div>
  </form>

</div>
