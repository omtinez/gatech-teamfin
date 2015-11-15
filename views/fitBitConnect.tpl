% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
    <h3>Enter your fitbit sharing id.</h3>
    <h5>Should look something like 9TQIQZ</h5>
	<form action="/fitBitConnect" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <input name="username" type="username" class="form-control" id="fitbit_id" placeholder="Enter Fit Bit Username">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Connect" type="submit" class="btn btn-default active" style = #ff0080/>
      </div>
    </div>
  </form>
</div>
