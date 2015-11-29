% rebase('layout.tpl', title='Sign Up')

<div class="jumbotron">
    <h1>JogRX</h1>
    <h3>Sign Up!</h3>
	<form action="/sign_up" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <input name="first_name" type="text" class="form-control" id="first_name" placeholder="First Name">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input name="last_name" type="text" class="form-control" id="last_name" placeholder="Last Name">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <select name="gender" type="text" class="form-control" id="gender" placeholder="Last Name">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input name="birthdate" type="date" class="form-control" id="birthdate" placeholder="Birthdate">
      </div>
    </div>
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
        <input value="Sign Up" type="submit" class="btn btn-primary active"/>
      </div>
    </div>
  </form>
</div>
