% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
    <h3>{{ message }}</h3>
	<form action="/login" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <input name="username" type="email" class="form-control" id="email" placeholder="Enter email">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">          
        <input name="password" type="password" class="form-control" id="pwd" placeholder="Enter password">
      </div>
    </div>

    <div class="form-group">        
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Login" type="submit" class="btn btn-default active"/>
      </div>
    </div>
  </form>
</div>

