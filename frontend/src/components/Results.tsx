import React, { useEffect, useState } from 'react';
import {
  Box,
  Button,
  Typography,
  Card,
  CardContent,
  CardActions,
  Grid,
  Chip,
  CircularProgress,
  Alert,
} from '@mui/material';
import axios from 'axios';

interface CardRecommendation {
  name: string;
  issuer: string;
  annual_fee: number;
  reward_type: string;
  reward_rate: number;
  key_benefits: string[];
  estimated_rewards: number;
  recommendation_reason: string;
  apply_link: string;
}

interface ResultsProps {
  formData: any;
  onReset: () => void;
}

const Results: React.FC<ResultsProps> = ({ formData, onReset }) => {
  const [recommendations, setRecommendations] = useState<CardRecommendation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await axios.post('http://localhost:8000/recommend', formData);
        if (response.data && Array.isArray(response.data)) {
          setRecommendations(response.data);
        } else {
          throw new Error('Invalid response format');
        }
      } catch (err: any) {
        console.error('Error fetching recommendations:', err);
        setError(err.response?.data?.detail || 'Failed to fetch recommendations. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [formData]);

  if (loading) {
    return (
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 4 }}>
        <CircularProgress />
        <Typography variant="body1" sx={{ mt: 2 }}>
          Finding the best credit cards for you...
        </Typography>
      </Box>
    );
  }

  if (error) {
    return (
      <Box sx={{ mt: 4, textAlign: 'center' }}>
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
        <Button variant="contained" onClick={onReset}>
          Try Again
        </Button>
      </Box>
    );
  }

  if (!recommendations.length) {
    return (
      <Box sx={{ mt: 4, textAlign: 'center' }}>
        <Alert severity="info" sx={{ mb: 2 }}>
          No credit cards found matching your preferences. Try adjusting your criteria.
        </Alert>
        <Button variant="contained" onClick={onReset}>
          Start Over
        </Button>
      </Box>
    );
  }

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" gutterBottom>
        Your Personalized Credit Card Recommendations
      </Typography>
      <Grid container spacing={3}>
        {recommendations.map((card, index) => (
          <Grid item xs={12} key={index}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {card.name}
                </Typography>
                <Typography color="textSecondary" gutterBottom>
                  {card.issuer}
                </Typography>
                <Box sx={{ mt: 2 }}>
                  <Typography variant="subtitle1" gutterBottom>
                    Key Benefits:
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                    {card.key_benefits.map((benefit, i) => (
                      <Chip 
                        key={i} 
                        label={benefit} 
                        size="small" 
                        color="primary"
                        variant="outlined"
                      />
                    ))}
                  </Box>
                </Box>
                <Box sx={{ mt: 2 }}>
                  <Typography variant="body2">
                    Annual Fee: ₹{card.annual_fee.toLocaleString()}
                  </Typography>
                  <Typography variant="body2">
                    Reward Rate: {card.reward_rate}%
                  </Typography>
                  <Typography variant="body2" color="primary" sx={{ fontWeight: 'bold' }}>
                    Estimated Annual Rewards: ₹{card.estimated_rewards.toLocaleString()}
                  </Typography>
                </Box>
                <Typography variant="body2" sx={{ mt: 2, color: 'text.secondary' }}>
                  {card.recommendation_reason}
                </Typography>
              </CardContent>
              <CardActions>
                <Button
                  size="small"
                  color="primary"
                  href={card.apply_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  variant="contained"
                >
                  Apply Now
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
      <Box sx={{ mt: 4, textAlign: 'center' }}>
        <Button variant="outlined" onClick={onReset}>
          Start Over
        </Button>
      </Box>
    </Box>
  );
};

export default Results; 