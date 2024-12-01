from .models        import *
from rest_framework import serializers

# ----- Genre Serializer -----
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = genre
        fields = ['name']

# ----- Actor Serializer -----
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = actor
        fields = ['first_name','last_name']

# ----- Director Serializer -----
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = director
        fields = ['first_name','last_name']

# ----- Producer Serializer -----
class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = producer
        fields = ['first_name','last_name']

# ----- Technician Serializer -----
class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model  = technician
        fields = ['name','role']

# ----- Movie Serializer with create and update methods -----
class MovieSerializer(serializers.ModelSerializer):
    genres      = GenreSerializer(many=True)
    actors      = ActorSerializer(many=True)
    directors   = DirectorSerializer(many=True)
    producers   = ProducerSerializer(many=True)
    technicians = TechnicianSerializer(many=True)

    class Meta:
        model  = movie
        fields = ['id','name','rating','release_date','genres','actors','directors','producers','technicians']

    def create(self,validated_data):
        genres_data      = validated_data.pop('genres')
        actors_data      = validated_data.pop('actors')
        director_data    = validated_data.pop('directors')
        producers_data   = validated_data.pop('producers')
        technicians_data = validated_data.pop('technicians')
        movie_data       = movie.objects.create(**validated_data)
        for gen in genres_data:
            genre_obj, _ = genre.objects.get_or_create(**gen)
            movie_data.genres.add(genre_obj)
        for act in actors_data:
            actor_obj, _ = actor.objects.get_or_create(**act)
            movie_data.actors.add(actor_obj)
        for dir in director_data:
            director_obj, _ = director.objects.get_or_create(**dir)
            movie_data.directors.add(director_obj)
        for tech in technicians_data:
            technician_obj, _ = technician.objects.get_or_create(**tech)
            movie_data.technicians.add(technician_obj)
        for pro in producers_data:
            producer_obj, _ = producer.objects.get_or_create(**pro)
            movie_data.producers.add(producer_obj)
        return movie_data
    
    def update(self,instance,validated_data):
        genres_data      = validated_data.pop('genres')
        actors_data      = validated_data.pop('actors')
        director_data    = validated_data.pop('directors')
        producers_data   = validated_data.pop('producers')
        technicians_data = validated_data.pop('technicians')
        for attr,val in validated_data.items():
            setattr(instance,attr,val)
        instance.save()
        if genres_data:      
            instance.genres.clear()
            for gen in genres_data:
                genre_obj , _ = genre.objects.get_or_create(**gen)
                instance.genres.add(genre_obj)
        if actors_data:
            instance.actors.clear()
            for act in actors_data:
                actor_obj , _ = actor.objects.get_or_create(**act)
                instance.actors.add(actor_obj)
        if director_data:
            instance.directors.clear()
            for dir in director_data:
                director_obj , _ = director.objects.get_or_create(**dir)
                instance.directors.add(director_obj)
        if producers_data:
            instance.producers.clear()
            for pro in producers_data:
                producer_obj , _ = producer.objects.get_or_create(**pro)
                instance.producers.add(producer_obj)
        if technicians_data:
            instance.technicians.clear()
            for tech in technicians_data:
                technician_obj , _ = technician.objects.get_or_create(**tech)
                instance.technicians.add(technician_obj)
        return instance