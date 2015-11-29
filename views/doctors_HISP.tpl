% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
	<h2>{{ title }}</h2>
	<h3>{{ message }}</h3>
	<form action="/doctors_HISP" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-10">
        <select name="hispAddress" class="form-control" placeholder="Where should we send your data?">
          <option value="" disabled selected>Where should we send your data?</option>
          <option value="http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base">Georgia Institute of Technology</option>
          <option value="https://open.epic.com/Interface/" disabled>Open Epic</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Submit" type="submit" class="btn btn-primary active"/>
      </div>
    </div>
  </form>

</div>
