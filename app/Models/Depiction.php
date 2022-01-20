<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Depiction extends Model
{
    use HasFactory;

    function paintings()
    {
        return $this->belongsToMany(Painting::class);
    }
}
