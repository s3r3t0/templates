```{=latex}
% {{ MANUAL_EDIT_WARNING }}
```

{% block description required %}{% endblock %}

{% if self.likelihood() | trim %}
#### Likelihood
{% endif %}

{% block likelihood %}{% endblock %}

{% if self.impact() | trim %}
#### Impact
{% endif %}

{% block impact %}{% endblock %}

{% if self.recommendation() | trim %}
#### Recommendation
{% endif %}

{% block recommendation %}{% endblock %}

{% if self.reference() | trim %}
#### References
{% endif %}

{% block reference %}{% endblock %}
