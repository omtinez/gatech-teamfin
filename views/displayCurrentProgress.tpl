% rebase('layout.tpl', title='Display Fitbit Data', year=year)
<div class="jumbotron">
<p>Steps taken today {{stepsTaken}} </p>
<p>Current Progress</p>
<div class="progress">
  <div class="progress-bar progress-bar-{{progress}} progress-bar-striped" role="progressbar"
  aria-valuenow="{{percentage}}" aria-valuemin="0" aria-valuemax="100" style="width:{{percentage}}%">
    <p>{{percentage}}% Complete</p>
  </div>
</div>
<br/>
</div>