% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
    <h3>{{ message }}</h3>
	<form action="/fitBitConnect" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <input name="username" type="username" class="form-control" id="username" placeholder="Enter Fit Bit Username">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Connect" type="submit" class="btn btn-default active" style = #ff0080/>
      </div>
    </div>
  </form>
</div>
